const env = {
    "development": {
        baseURL: "http://localhost:8000/api/"
    },
    "production": {
        baseURL: "https://vocabin.net/api/"
    }
}

export default env[process.env.NODE_ENV || "development"]
