$(function() {
    //Title
    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip();
    });

    /* Muda a Cor do Menu */
    var menu = document.getElementById('menu'); // colocar em cache
    var menu2 = document.getElementById('menu2'); // colocar em cache

    window.addEventListener('scroll', function () {
        if ((window.scrollY > 0) && (menu != null)){
            menu.classList.add('novoMenu'); // > 0 ou outro valor desejado


            $("div").mouseover(function () {
                var ID = this.id;

                if(ID == 'coworking'){
                    $('.navbar-nav>#1').removeClass('active');
                    $('.navbar-nav>#2').addClass('active');
                    $('.navbar-nav>#3').removeClass('active');
                    $('.navbar-nav>#4').removeClass('active');
                    $('.navbar-nav>#5').removeClass('active');
                }

                else if(ID == 'planos'){
                    $('.navbar-nav>#1').removeClass('active');
                    $('.navbar-nav>#2').removeClass('active');
                    $('.navbar-nav>#3').addClass('active');
                    $('.navbar-nav>#4').removeClass('active');
                    $('.navbar-nav>#5').removeClass('active');
                }

                else if(ID == 'vilaMarieta'){
                    $('.navbar-nav>#1').removeClass('active');
                    $('.navbar-nav>#2').removeClass('active');
                    $('.navbar-nav>#3').removeClass('active');
                    $('.navbar-nav>#4').addClass('active');
                    $('.navbar-nav>#5').removeClass('active');
                }

                else if(ID == 'contato'){
                    $('.navbar-nav>#1').removeClass('active');
                    $('.navbar-nav>#2').removeClass('active');
                    $('.navbar-nav>#3').removeClass('active');
                    $('.navbar-nav>#4').removeClass('active');
                    $('.navbar-nav>#5').addClass('active');
                }

                else {
                    $('.navbar-nav>li').removeClass('active');
                }

            });

        }
        else {
            if(menu != null){
                $('.navbar-nav>#1').removeClass('active');
                menu.classList.remove('novoMenu');
            }
        }
    });

    /* Velocidade do Menu */
    $("#menu .navbar-nav a[href^='#']").on('click', function(e) {
		e.preventDefault();
		var hash = this.hash;
		$('html, body').animate({
			scrollTop: $(this.hash).offset().top
		}, 600);
	});

    /* Rodape */
    $('#back-to-top').on('click', function(){
		$('body,html').animate({
			scrollTop: 0
		}, 600);
	});

    $(window).on('scroll', function() {
		var wScroll = $(this).scrollTop();
		wScroll > 1 ? $('#nav').addClass('fixed-nav') : $('#nav').removeClass('fixed-nav');
		wScroll > 500 ? $('#back-to-top').fadeIn() : $('#back-to-top').fadeOut();
	});

});
