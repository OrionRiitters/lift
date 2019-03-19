addHomeHandlers();

function addHomeHandlers() {
    $('#btn-1').on('click', function(e) {
        $.get('/templates/start_workout.html', function( data ) {
            $('body').html( data );
            addHomeHandlers();
        });
    });

    $('#btn-2').on('click', function(e) {
        $.get('/templates/view_stats.html', function( data ) {
            $('body').html( data );
            addHomeHandlers();
        });
    });

    $('#btn-3').on('click', function(e) {
        $.get('/templates/create_new.html', function( data ) {
            $('body').html( data );
            addHomeHandlers();
        });
    });

}
