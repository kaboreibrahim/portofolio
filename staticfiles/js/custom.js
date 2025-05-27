
window.onload = typeTitle;

document.addEventListener('DOMContentLoaded', function () {
    // Fonction pour vérifier si une image existe
    function imageExists(url, callback) {
        var img = new Image();
        img.onload = function () { callback(true); };
        img.onerror = function () { callback(false); };
        img.src = url;
    }

    // Remplacer les images manquantes par des placeholders
    var techItems = document.querySelectorAll('.tech-item img');
    techItems.forEach(function (img) {
        var imgSrc = img.getAttribute('src');
        var techName = img.getAttribute('alt');

        imageExists(imgSrc, function (exists) {
            if (!exists) {
                // Créer un placeholder avec le nom de la technologie
                var canvas = document.createElement('canvas');
                canvas.width = 150;
                canvas.height = 80;
                var ctx = canvas.getContext('2d');

                // Définir un dégradé de couleur basé sur le nom de la technologie
                var hash = 0;
                for (var i = 0; i < techName.length; i++) {
                    hash = techName.charCodeAt(i) + ((hash << 5) - hash);
                }

                var color1 = '#' + ((hash & 0x00FFFFFF) | 0x004080).toString(16).substr(1);
                var color2 = '#' + ((hash & 0x00FFFFFF) | 0x408000).toString(16).substr(1);

                var gradient = ctx.createLinearGradient(0, 0, 150, 80);
                gradient.addColorStop(0, color1);
                gradient.addColorStop(1, color2);

                ctx.fillStyle = gradient;
                ctx.fillRect(0, 0, 150, 80);

                // Ajouter le texte
                ctx.fillStyle = 'white';
                ctx.font = 'bold 16px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(techName, 75, 40);

                // Remplacer l'image par le canvas
                img.src = canvas.toDataURL('image/png');
            }
        });
    });

    // Pause de l'animation au survol
    var carousel = document.querySelector('.tech-carousel');
    var carouselTrack = document.querySelector('.tech-carousel-track');

    carousel.addEventListener('mouseenter', function () {
        carouselTrack.style.animationPlayState = 'paused';
    });

    carousel.addEventListener('mouseleave', function () {
        carouselTrack.style.animationPlayState = 'running';
    });
});

