let moving_elements = document.getElementsByClassName('move')
function abs(x) {
    if (x < 0) return -x
    else return x
}

for (var i = 0; i < moving_elements.length; i++) {
    let el = moving_elements[i]
    el.onmouseenter = (ev) => {
        if (ev.movementX == 0 || abs(ev.movementY) > abs(ev.movementX)) { return }

        let right = ev.movementX > 0
        let to_remove = right ? 'left' : 'right'
        let to_add = right ? 'right' : 'left'

        el.classList.remove(to_remove)
        el.classList.add(to_add)
    }
    el.onmouseleave = el.onmouseenter
}

let body = document.getElementsByTagName('body')[0]
let start_offset = 0
let parallax_factor = 2
body.style.backgroundPositionY = `-${ start_offset }px`

window.onscroll = () => {
    let offset = window.scrollY
    body.style.backgroundPositionY = `-${ start_offset + offset / parallax_factor }px`
}

function select_slideshow_label(el) {
    let siblings = el.parentElement.children
    for (var e of siblings) {
        e.classList.remove('active')
    }
    el.classList.add('active')
}