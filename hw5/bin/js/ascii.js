(function() {
  $(function() {
    var animation, autoPlay, frame, frameContainer, interval, itv;
    animation = false;
    frameContainer = [];
    interval = null;
    frame = -1;
    itv = 200;
    $('#small').click(function() {
      return $('#displayarea').css('fontSize', '7pt');
    });
    $('#medium').click(function() {
      return $('#displayarea').css('fontSize', '12pt');
    });
    $('#large').click(function() {
      return $('#displayarea').css('fontSize', '24pt');
    });
    $('#animation').change(function() {
      $('#displayarea').val(ANIMATIONS[$('#animation').val()]);
      animation = false;
      return frame = -1;
    });
    $('#start').click(function() {
      if (!animation) {
        frameContainer = $('#displayarea').val().split('=====\n');
        interval = setInterval(autoPlay, itv);
        animation = true;
        $('#stop').attr('disabled', false);
        $('#start').attr('disabled', true);
        return $('#animation').attr('disabled', true);
      }
    });
    $('#stop').click(function() {
      if (animation) {
        clearInterval(interval);
        animation = false;
        frame = -1;
        $('#displayarea').val(ANIMATIONS[$('#animation').val()]);
        $('#stop').attr('disabled', true);
        $('#start').attr('disabled', false);
        return $('#animation').attr('disabled', false);
      }
    });
    $('#speed').click(function() {
      itv = $('#speed').attr('checked') === 'checked' ? 50 : 200;
      if (animation) {
        return clearInterval(interval, interval = setInterval(autoPlay, itv));
      }
    });
    return autoPlay = function() {
      $('#displayarea').val(frameContainer[++frame]);
      if (frame === frameContainer.length - 1) {
        return frame = -1;
      }
    };
  });

}).call(this);
