console.log('HELLO PROFILE TEACHER');

const modifyTeacher = document.getElementById("teacher-modify");
const accountForm = document.getElementById("account-form");
const notifyAccount = document.getElementById("notify-account");
const url = window.location.href;

$.ajax({
    type: 'GET',
    url: `${url}get-infor`,
    success: function(response) {
        const avatar = response['avatar'];
        const name = response['name'];
        const gender = response['gender'];
        const email = response['email'];

        $("#avatarDemo").attr("src", avatar);
        $('#id_name').attr('value', name);
        $(`#id_gender option[value=${gender}]`).attr("selected", "selected");
        $("#id_email").attr("value", email);
        console.log(response);
    },
    error: function(response) {
        console.log(response);
    },
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