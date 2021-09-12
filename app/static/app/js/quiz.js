console.log('working....')

// Hiding alert box
$('#msg').delay(3000).hide(0);

function section(id) {
    console.log(id);
    var last;
    document.getElementById(id).addEventListener('input', (e) => {
        console.log('called', e.target.getAttribute('name') == "answer");
        if (e.target.getAttribute('name') == "answer") {
            if (last)
                last.checked = false;
        }
        e.target.checked = true;
        last = e.target;
    })
}


