var firstname = prompt("Please enter your first name")
var lastname = prompt("Please enter your last name")
var age = prompt("Please enter your age")
var height = prompt("Pleaes tell me how tall you are in 'cm'")
var pet = prompt("Please enter your pet's name")
// var firstcheck = firstname.slice(0, 1)
// var lastcheck = lastname.slice(0, 1)
// var petcheck = pet.slice(-1)

var firstcheck = firstname[0]
var lastcheck = lastname[0]
var petcheck = pet[pet.length-1]

console.log(firstcheck)
console.log(lastcheck)
console.log(petcheck)

if (firstcheck === lastcheck && age > 20 && age < 30 && height >= 170 && petcheck === "y") {
    console.log("You are the spy");
} else {
    console.log("Thank you");
}
