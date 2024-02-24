;
var p = {
    name: "Ahmed",
    age: 39,
    cars: ['BMW',],
};
function displayPerson(p) {
    return JSON.stringify(p);
}
var res = displayPerson(p);
console.log(res);
