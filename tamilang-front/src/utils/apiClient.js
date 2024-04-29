
const url = "http://localhost:3000"
export default class ApiClient {
    constructor() {
        
    }
    async getLetters() {
        const res = await fetch(`${url}/api/letters`);
        if (!res.ok) {
            throw new Error("Failed to fetch data");
          }
          return res.json();
    }
}