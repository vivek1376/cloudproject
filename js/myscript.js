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

                movieCount = Math.min(10, movieList.length);

                for (var i = 0; i < movieCount; i++) {
                    var movie_div = document.createElement('div');
                    movie_div.setAttribute('class', 'movie clearfix');
                    // movie_div.setAttribute('class', '.clearfix');

                    var poster_url = 'https://image.tmdb.org/t/p/w92/' + movieList[i]['posterid'];
                    var movie_poster_img = document.createElement('img');
                    movie_poster_img.setAttribute('src', poster_url);
                    movie_poster_img.setAttribute('class', 'movieimg');

                    movie_div.appendChild(movie_poster_img);

                    var movie_imdb_a = document.createElement('a');
                    movie_imdb_a.setAttribute('href', 'https://www.imdb.com/title/' + movieList[i]['imdbid']);
                    movie_imdb_a.setAttribute('class', 'imdbid');
                    movie_imdb_a.setAttribute('target', '_blank');
                    textnode = document.createTextNode("imdb \uD83E\uDC6D");
                    movie_imdb_a.appendChild(textnode);
                    movie_div.appendChild(movie_imdb_a);

                    var movie_title_overview_p = document.createElement('p');
                    movie_title_overview_p.setAttribute('class', 'titleoverview');

                    var movie_title_p = document.createElement('p');
                    var textnode = document.createTextNode(movieList[i]['title']);
                    movie_title_p.appendChild(textnode);
                    movie_title_p.setAttribute('class', 'movietitle');

                    movie_title_overview_p.appendChild(movie_title_p);

                    movie_overview_p = document.createElement('p');
                    movie_overview_p.setAttribute('class', 'overview');
                    textnode = document.createTextNode(movieList[i]['overview']);
                    movie_overview_p.appendChild(textnode);

                    movie_title_overview_p.appendChild(movie_overview_p);

                    movie_div.appendChild(movie_title_overview_p);

                    if (i === 0) {
                        movie_div.setAttribute('class', 'movie clearfix firstmovie');
                    } else if (i === (movieCount - 1)) {
                        movie_div.setAttribute('class', 'movie clearfix lastmovie');
                    }

                    document.querySelector('div.movielist').appendChild(movie_div);

                    // console.log(movieList[i]);
                }

            })
            .on('500', function () {
                document.querySelector('div.movielist').innerHTML = "";
                document.querySelector('div.movielist').innerHTML = "Error occurred. please try again!";
            })
            .go();
        console.log("clicked");
    });
});