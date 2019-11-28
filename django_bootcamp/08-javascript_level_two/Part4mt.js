// Create roster array
var roster = []

//Alert if user would like to use the app
var willUse = prompt("Would you like to use roster web app? y/n");
if (willUse === 'y') {
    rosterFunc();
} else {
    goodBy();
}


function rosterFunc() {
    // TODO: program
    while (true) {
        var userComm = prompt('Please input the command, "add", "remove", "display" or "quit"');
        if (userComm === 'add') {
            addStudent();
        } else if (userComm === 'remove') {
            removeStudent();
        } else if (userComm === 'display') {
            displayStudent();
        } else if (userComm === 'quit') {
            goodBy();
            break;
        } else {
            alert("Please enter correct command.");
            continue;
        }
    }
}

function addStudent() {
    var name = prompt("Please enter the student's name to add.");
    roster.push(name);
}

function removeStudent(name) {
    var name = prompt ("Please enter the student's name to remove.");
    var index = roster.indexOf(name);
    if (index > -1) {
        roster.splice(index, 1);
    }
}

function displayStudent() {
    console.log(roster);
}

function goodBy() {
    alert("Thank you for using roster web app.  " +
        "Please reload the page to restart.");
}
