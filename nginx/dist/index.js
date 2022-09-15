const button = document.getElementById('sender')
const placeholder = document.getElementById('placeholder')

button.addEventListener('click', () => {
    fetch('http://localhost/api/super/path_label/files?query_label=default')
        .then(res => {
            console.log(res)
            return res.json()
        })
        .then(json => placeholder.innerHTML = `${json['url']} ${json['code']}`)
        .catch(err => {
            placeholder.innerHTML = err
            console.log(err)
        })
})