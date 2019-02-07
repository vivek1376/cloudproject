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
                console.log(response);

                var movieList = response['list'];

                // clear
                document.querySelector('div.movielist').innerHTML = "";

                for (var i = 0; i < movieList.length; i++) {
                    var movie_div = document.createElement('div');
                    movie_div.setAttribute('class', 'movie clearfix');
                    // movie_div.setAttribute('class', '.clearfix');

                    var poster_url = 'https://image.tmdb.org/t/p/w92/' + movieList[i]['posterid'];
                    var movie_poster_img = document.createElement('img');
                    movie_poster_img.setAttribute('src', poster_url);
                    movie_poster_img.setAttribute('class', 'movieimg');

                    movie_div.appendChild(movie_poster_img);


                    var movie_title_p = document.createElement('p');
                    var textnode = document.createTextNode(movieList[i]['title']);
                    movie_title_p.appendChild(textnode);
                    movie_title_p.setAttribute('class', 'movietitle');

                    movie_div.appendChild(movie_title_p);

                    var movie_imdb_a = document.createElement('a');
                    movie_imdb_a.setAttribute('href', 'https://www.imdb.com/title/' + movieList[i]['imdbid']);
                    movie_imdb_a.setAttribute('class', 'imdbid');
                    movie_imdb_a.setAttribute('target', '_blank');

                    textnode = document.createTextNode("imdb \uD83E\uDC6D");
                        // movieList[i]['imdbid']);
                    movie_imdb_a.appendChild(textnode);
                    // movie_imdb_a.innerText="imdb \u1f86d";
                    // movie_imdb_p.setAttribute('class', 'imdbid');

                    movie_div.appendChild(movie_imdb_a);



                    //
                    document.querySelector('div.movielist').appendChild(movie_div);

                    // console.log(movieList[i]);
                }

            })
            .go();
        console.log("clicked");
    });
});