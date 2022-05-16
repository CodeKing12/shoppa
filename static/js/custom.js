const csrftoken = getCookie('csrftoken');
    // if (document.readyState !== "loading") {
    //     loading = false
// }
    // loadicons.push(loadicons[icon])
    // console.log(delay_num)
// }

// function dontSubmit(element) {
//     element.preventDefault();
// }

if (document.readyState === "complete") { console.log("Complete") }

const notyf = new Notyf({
    duration: 10000,
    position: {
        x: 'center',
        y: 'top',
    },
    // dismissible: true,
    types: [
        {
           type: 'warning',
            background: '#cea605',
            icon: "<span class='material-symbols-outlined' style='color:white;vertical-align:middle'>warning</span>",
            duration: 3000,
            dismissible: true
        },
        {
            type: 'info',
            background: '#2d2dbf',
            icon: "<span class='material-symbols-outlined' style='color:white;vertical-align:middle'>info</span>",
            duration: 3000,
            dismissible: true
        },
        {
            type: 'error',
            background: 'indianred',
            duration: 2000,
            dismissible: true
        },
        {
            type: 'success',
            duration: 2000,
            dismissible: true
        }
    ]
});

function openModal() {
    $('#sign-in').modal()
}

function showNotice() {
    notyf.open({
        type: "warning",
        message: "You  must log in to use this feature",
        duration: 5000,
    });
}

function openLogin(message, type, duration=8000) {
    $('#sign-in').modal();
    notyf.open({
        type: type,
        message: message,
        duration: duration,
    });
    // console.log("{{open_login}}")
}

function processResponse(response) {
    // console.log(response);
    let message;
    let alert_type;
    if (typeof(response['responseJSON']) == 'undefined') {
        message = response['message'];
        alert_type = response['type'];
    } else {
        message = response['responseJSON']['message'];
        alert_type = response['responseJSON']['type'];
    };
    if (typeof(message) == 'undefined') {
        message = 'An Error Occurred. Please Try Again'
        alert_type = 'error'
        console.log(response)
        // location.reload()
    }
    if (typeof(message) == 'object') {
        for (const error in message) {
            error_message = message[error]
            notyf.open({
                type: alert_type,
                message: error_message,
                duration: 7000,
            });
        }
    } else {
        notyf.open({
            type: alert_type,
            message: message,
            duration: 7000,
        });
    }
    return true;
}

function showForm(modalName) {
    $(".sign-in-modal-close").click();
    $(`#${modalName}`).modal();
}

// http://127.0.0.1:1112/account/change-password/MTA/b5hzij-5bb9294c89210100fe114fe18e3186b5