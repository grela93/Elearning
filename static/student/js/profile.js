console.log('hello profile');

const inforBtn = document.getElementById("infor-btn");
const modifyBtn = document.getElementById("modify-btn");
const inforArrow = document.getElementById("arrow-infor");
const modifyArrow = document.getElementById("arrow-modify");
const inforStudent = document.getElementById("student-infor");
const modifyStudent = document.getElementById("student-modify");
const accountForm = document.getElementById("account-form");
const inforForm = document.getElementById("infor-form");
const notifyAccount = document.getElementById("notify-account");
const notifyInfor = document.getElementById("notify-infor");
const url = window.location.href;

inforArrow.classList.add("bx-fade-right", "arrow-active");
modifyStudent.classList.add("not-visible");

inforBtn.addEventListener("click", (e) => {
    inforStudent.classList.remove("not-visible");
    modifyStudent.classList.add("not-visible");

    inforArrow.classList.add("bx-fade-right", "arrow-active");
    modifyArrow.classList.remove("bx-fade-right", "arrow-active");
});

modifyBtn.addEventListener("click", (e) => {
    inforStudent.classList.add("not-visible");
    modifyStudent.classList.remove("not-visible");

    inforArrow.classList.remove("bx-fade-right", "arrow-active");
    modifyArrow.classList.add("bx-fade-right", "arrow-active");

    $.ajax({
        type: 'GET',
        url: `${url}get-infor`,
        success: function(response) {
            const avatar = response['avatar'];
            const name = response['name'];
            const school_year = response['school_year'];
            const gender = response['gender'];
            const phone = response['phone'];
            const email = response['email'];
            const address = response['address'];
            $("#avatarDemo").attr("src", avatar);
            $('#id_name').attr('value', name);
            $("#id_school_year").attr("value", school_year);
            $(`#id_gender option[value=${gender}]`).attr("selected", "selected");
            $("#id_phone").attr("value", phone);
            $("#id_email").attr("value", email);
            $("#id_address").attr("value", address);
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        },
    })
});

const csrf = document.getElementsByName("csrfmiddlewaretoken");

const modifyAccount = () => {
    const username = document.getElementById("usernameMod");
    const password = document.getElementById("passwordMod");

    data = {};
    data["csrfmiddlewaretoken"] = csrf[0].value;
    data['username'] = username.value;
    data['password'] = password.value;

    $.ajax({
        type: "POST",
        url: `${url}modify-account`,
        data: data,
        success: function (response) {
            notifyAccount.innerHTML = "Sửa tài khoản thành công!"
            console.log(response);
        },
        error: function (response) {
            console.log(response);
        },
    });
}

accountForm.addEventListener('submit', (e) => {
    e.preventDefault();

    modifyAccount();
})
// const modifyInfor = () => {
//     const avatar = document.getElementById("id_avatar");
//     const name = document.getElementById("nameMod");
//     const schoolYear = document.getElementById("schoolYearMod");
//     const gender = document.getElementById("genderMod");
//     const phone = document.getElementById("phoneMod");
//     const email = document.getElementById("emailMod");
//     const address = document.getElementById("addressMod");

//     data = {};
//     data["csrfmiddlewaretoken"] = csrf[0].value;
//     data["avatar"] = avatar.value;
//     data["name"] = name.value;
//     data["schoolYear"] = schoolYear.value;
//     data["gender"] = gender.value;
//     data["phone"] = phone.value;
//     data["email"] = email.value;
//     data["address"] = address.value;

//     $.ajax({
//         type: "POST",
//         url: `${url}modify-infor`,
//         data: data,
//         success: function (response) {
//             // $("#avatarDemo").attr('src', )
//             console.log(response);
//         },
//         error: function (response) {
//             console.log(response);
//         },
//     });
// };


// inforForm.addEventListener('submit', (e) => {
//     e.preventDefault();

//     modifyInfor();
// })