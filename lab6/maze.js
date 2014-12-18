// Generated by CoffeeScript 1.8.0
(function() {
  $(function() {
    var lose, youLose;
    youLose = false;
    lose = function() {
      if (!youLose) {
        $('.boundary').addClass('youlose');
        $('#status').html('You lose!');
        return youLose = true;
      }
    };
    $('.boundary').mouseover(function() {
      return lose();
    });
    $('#maze').mouseleave(function() {
      return lose();
    });
    $('#start').click(function() {
      $('.boundary').removeClass('youlose');
      return youLose = false;
    });
    return $('#end').mouseover(function() {
      if (!youLose) {
        $('#status').html('You win!');
        return youLose = true;
      }
    });
  });

}).call(this);