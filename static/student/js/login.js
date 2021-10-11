const sign_in_student_btn = document.querySelector("#sign-in-student-btn");
const sign_in_teacher_btn = document.querySelector("#sign-in-teacher-btn");
const container = document.querySelector(".container");

sign_in_teacher_btn.addEventListener("click", () => {
    container.classList.add("sign-in-teacher-mode");
});

sign_in_student_btn.addEventListener("click", () => {
    container.classList.remove("sign-in-teacher-mode");
});
