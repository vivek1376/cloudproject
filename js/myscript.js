document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('input#submit').addEventListener("click", function () {
        aja()
            .method('POST')
            .url('/')
            .timeout(2500)
            .data({'val1':'1','val2':'2'})
            .on('200', function (response) {
                console.log('ajax response received!!');
            })
            .go();
        console.log("clicked");
    });
});