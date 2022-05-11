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