// Credit to the inspiration behind this to Richard Codes' YouTube resource:
// How to Style Select Tags, Create Custom Dropdown | HTML CSS Javascript
// https://www.youtube.com/watch?v=ceveRz3e7F0&t=1077s 

const raceButton = document.querySelector('#race-button');
const genderButton = document.querySelector('#gender-button');

const selectRace = document.querySelector("#race-dropdown");
const selectGender = document.querySelector("#gender-dropdown");

const options = document.querySelectorAll(".option");
const genOptions = document.querySelectorAll(".gen-option");

const selectRaceLabel = document.querySelector('#select-label-race');
const selectGenLabel = document.querySelector('#select-label-gender');


raceButton.addEventListener("click", function (e) {
	e.preventDefault();
  toggleHiddenRace();
});

function toggleHiddenRace() {
	selectRace.classList.toggle("hidden");
}

genderButton.addEventListener("click", function (e) {
	e.preventDefault();
  toggleHiddenGender();
});

function toggleHiddenGender() {
	selectGender.classList.toggle("hidden");
}


options.forEach(function(option) {
	option.addEventListener("click", function (e) {
		setRaceTitle(e);
	});
});

function setRaceTitle(e) {
	const labelRaceElement = document.querySelector(`label[for="${e.target.id}"]`).innerText;
	selectRaceLabel.innerText = labelRaceElement;
	toggleHiddenRace();
};


genOptions.forEach(function(genOption) {
	genOption.addEventListener("click", function (e) {
		setGenderTitle(e);
	});
});

function setGenderTitle(e) {
	const labelGenElement = document.querySelector(`label[for="${e.target.id}"]`).innerText;
	selectGenLabel.innerText = labelGenElement;
	toggleHiddenGender();
};