        var magnifPopup = function() {
            $('.popup-img').magnificPopup({
                type: 'image',
                removalDelay: 300,
                mainClass: 'mfp-with-zoom',
                gallery: {
                    enabled: true
                },
                zoom: {
                    enabled: true,

                    duration: 300,
                    easing: 'ease-in-out',
                    opener: function(openerElement) {

                        return openerElement.is('img') ? openerElement : openerElement.find('img');
                    }
                }
            });
        };


        if ($('.overlay')[0]) {

            $('.overlay').magnificPopup({
                delegate: 'a',
                type: 'image',
                gallery: {
                    enabled: true
                }
            });
        }


        // Call the functions 
        magnifPopup();