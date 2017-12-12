function main() {
    var input = document.getElementById("queryStudent").value;
    return "{% url_for('/query/Student/<id>'), id=input %}";
}