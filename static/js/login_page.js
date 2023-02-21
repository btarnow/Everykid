"use strict";

const signUpLogInText = document.querySelector('.toggle-signup');

signUpLogInText.addEventListener('click', (evt) => {
    toggleSignUpLogIn(evt);
})

function toggleSignUpLogIn (evt) {
    const loginForm = document.querySelector(".login-form");
    const signUpForm = document.querySelector(".sign-up-form");
    const viewLogin = signUpForm.classList.contains("form-hidden");

    if (viewLogin) {
        loginForm.classList.add("form-hidden");
        signUpForm.classList.remove("form-hidden");
        signUpLogInText.innerHTML = "Already have an account? <span class='blue'>Log in</span>";
    } else {
        loginForm.classList.remove("form-hidden");
        signUpForm.classList.add("form-hidden");
        signUpLogInText = "Don't have an account? <span class='blue'>Sign Up</span>";
    }
}