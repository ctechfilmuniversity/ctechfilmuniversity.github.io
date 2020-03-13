(function() {
    //get parameter by name
    function getQueryVariable(variable) {
        var query = window.location.search.substring(1);
        var vars = query.split('&');
    
        for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
    
        if (pair[0] === variable) {
            return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
        }
    }
    
    var searchTerm = getQueryVariable('query');

    // perform search 
    if (searchTerm) {
        document.getElementById('search-box').setAttribute("value", searchTerm);

        console.log(ctech_searchindex);

        // Initalize lunr with the fields it will be searching on. I've given title
        // a boost of 10 to indicate matches on this field are more important.
        var idx = lunr(function () {
            this.ref('id');
            this.field('title', { boost: 10 });
            this.field('author');
            this.field('category');
            this.field('tag');
            this.field('content');
            //this.metadataWhitelist = ['position']; // show positions of search terms

            ctech_searchindex.forEach(function (doc) {
              this.add(doc);
            }, this);
        });

        var results = idx.search(searchTerm); // Get lunr to perform a search
        displaySearchResults(results, ctech_searchindex); // We'll write this in the next section
    }

    //display

    function displaySearchResults(results, store) {
        var searchResults = document.getElementById('search-results');

        console.log(results);
    
        if (results.length) { // Are there any results?
            var appendString = '';
            for (var i = 0; i < results.length; i++) {  // Iterate over the results
                var item = store[results[i].ref];
  
                appendString += '<a href="' + item.url + '"><div>';
                let coverImageHTML = '<div class="search-image visible-desktop" ';
                if (item.coverImage !== null && item.coverImage.length > 0) {
                    coverImageHTML += 'style="background-image:url(/assets/img/' + item.coverImage + '")>';
                } else {
                    coverImageHTML += 'style="background-image:url(/assets/img/CTech_Originals/ctech-header-2.png")>';
                }
                coverImageHTML += '</div>';
                appendString += coverImageHTML; // desktop

                appendString+= '<div class="txtwrapper">';
                appendString += '<h2>' + item.title + "</h2>";
                appendString += coverImageHTML.replace("visible-desktop", "visible-mobile"); // mobile

                

                appendString += '<p>' + item.content.substring(0, 280) + '...</p>';
                appendString += '</div></div></a>';
                //appendString += '<p>' + item.content.substring(0, 150) + '...</p></article>';

                // too much effort right now to show exact position of search terms
                // if ("matchData" in results[i]) {
                //     let meta = results[i].matchData;
                //     let position = [];
                //     while (true) {
                //         if (Object.keys(meta).length > 0) {
                //             meta = meta[Object.keys(meta)[0]];
                //         } else {
                //             position = meta;
                //             break;
                //         }
                //     }
                // }
            }
            searchResults.innerHTML = appendString;
        } else {
            searchResults.innerHTML = '<div class="noresults"><p>No results found<p></div>';
        }
    }

})();