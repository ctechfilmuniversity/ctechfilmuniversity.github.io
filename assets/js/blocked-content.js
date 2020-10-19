    window.onload = function() {
        if (getCookie("allowThirdParty") === "1") {
            // unblock videos
            unblockVideos();   
        }
    };
    

    function unblockVideos() {
        document.querySelectorAll('.video-container.blocked').forEach(element => {
            element.classList.remove("blocked");
            let uri = element.querySelector("iframe").getAttribute("data-src");
            element.querySelector("iframe").setAttribute('src', uri);
        });
    }

    function setAllowThirdParty() {
        setCookie("allowThirdParty", "1", 365);
        unblockVideos();
    }

    function setCookie(cname, cvalue, exdays) {
        let d = new Date();
        d.setTime(d.getTime() + (exdays*24*60*60*1000));
        let expires = "expires="+ d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/; SameSite=Strict";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i = 0; i <ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) == ' ') {
            c = c.substring(1);
          }
          if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
          }
        }
        return "";
    }

