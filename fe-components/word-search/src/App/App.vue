<style>
  @import './App.scss';
</style>

<template>
    <div class="App">
        <TopSearch
            v-if="response || loading"
            @search="search"
            @optionsChange="onOptionsChange"
        >
        </TopSearch>
        <section class="section float-section" v-if="!response && !loading">
            <FloatingSearch
                @search="search"
                @optionsChange="onOptionsChange"
            >
            </FloatingSearch>
        </section>

        <section class="section mid-section">
            <article v-if="!showSectionBox">
              <div class="card" style="border-left: 3px solid #3273dc; padding: 1em;">
                <p><b>Vocabin</b> is a language-learning tool which shows example sentences for each inflection of a given word.
                Sentences can be filtered by difficulty level and category.</p>
                <p style="padding-top: 0.5em;">Select your target language from the dropdown, then search a word in that language to try it out!</p>
              </div>
            </article>
            <div v-if="showSectionBox">
                <div v-if="errorMessage">
                    <ErrorCard :message="errorMessage"></ErrorCard>
                </div>
                <div v-if="loading && !errorMessage">
                    <div class="box">
                        <i class="fas fa-list head-icon"></i>
                        Fetching results...
                    </div>
                </div>
                <div v-else-if="!loading && !noResults">
                    <Conjugations :response="response" @search="altSearch">
                </div>
                <div v-else-if="noResults" class="box">
                    No results found for "{{ response.forms[0] }}"!
                </div>
            </div>
        </section>

    </div>
</template>

<script>
import vocaAPI from "../api";
import Conjugations from "../Conjugations/Conjugations";
import ErrorCard from "../ErrorCard/ErrorCard";
import FloatingSearch from "../FloatingSearch/FloatingSearch";
import TopSearch from "../TopSearch/TopSearch.vue";
import { noResults } from "../utils";
import Vue from "vue";
import "reflect-metadata";
import { Component, ProvideReactive } from "vue-property-decorator";

const components = {
    Conjugations,
    ErrorCard,
    FloatingSearch,
    TopSearch,
};

@Component({ components })
export default class App extends Vue {

    response: any = null;
    loading = false;
    noResults = false;
    errorMessage: string | null = null;
    showTooltip = false;

    @ProvideReactive() searchTerm: string | null = null;
    @ProvideReactive() lang: string = "en";
    @ProvideReactive() difficulty: string = "";
    @ProvideReactive() category: string = "";

    get showSectionBox() {
        return this.response || this.noResults || this.loading;
    }

    search(searchTerm) {
        this.searchTerm = searchTerm;
        this.get();
    }

    altSearch(group) {
        this.get(group);
    }

    onOptionsChange(options) {
        this.lang = options.lang;
        this.difficulty = options.difficulty;
        this.category = options.category;
    }

    /* Fetch sentences for a given search term (word) and store in this.response */
    async get(group?: string) {
        this.loading = true;
        this.resetParams();
        const qParams = group ? { group } : {};
        try {
            const res = await vocaAPI.get(`forms/${this.lang}/${this.searchTerm}/`, qParams);
            if (res.data["forms"].length === 0) {
                this.noResults = true;
            }
            this.response = res.data;
            this.loading = false;
        } catch(e) {
            this.handleErr(e);
        }
    }

    handleErr(e) {
       this.errorMessage = e.message;
    }

    /* Set the search/response params back to initial state */
    resetParams() {
        this.noResults = false;
        this.errorMessage = null;
        this.response = null;
    }
}
</script>
