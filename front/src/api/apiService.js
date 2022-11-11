import http from "./Httpcommon";
class apiService {
  getdata(filtertype, input) {
    return http.get("/api/" + filtertype + "/" + input);
  }
}
export default new apiService();
