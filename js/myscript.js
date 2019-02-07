document.addEventListener("DOMContentLoaded", function() {

    document.querySelector('input#submit').addEventListener("click", function () {
        var selectObj = document.querySelector('select#genrelist');
        var selectOpt_val = selectObj.options[selectObj.selectedIndex].value;

        console.log("selectOpt: " + selectOpt_val);

        var yr = document.querySelector('input#yearbox').value;

        aja()
            .method('POST')
            .url('/')
            .timeout(2500)
            .data({'genreid': selectOpt_val,'relyear': yr})
            .on('200', function (response) {
                console.log('ajax response received!!\n');// + JSON.stringify(response['results']));

                var movieList = response['results'];

                for (var i = 0; i < movieList.length; i++) {
                    var movie_div = document.createElement('div');
                    var textnode = document.createTextNode(movieList[i]['original_title']);
                    movie_div.appendChild(textnode);
                    movie_div.setAttribute('class', 'movie');

                    document.querySelector('div.movielist').appendChild(movie_div);

                    console.log(movieList[i]);
                }

            })
            .go();
        console.log("clicked");
    });
});