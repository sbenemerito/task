(function($) {
    $(document).ready(function () {
        $('#id_model_b').change(function() {
            var b_ids = $(this).val();
            var c_ids = $('#id_model_c').val();
            var params = {
                'b': b_ids,
                'c': c_ids
            };

            $.ajax({
                url: '/retrieve_options/',
                data: params,
                dataType: 'json',
                success: function (data) {
                  var newOptions = '';
                  for (var i = 0; i < data.a_options.length; i++) {
                    newOptions += ('<option value="' +data.a_options[i][0]+ '">' +data.a_options[i][1]+ '</option>');
                  }
                  document.getElementById('id_model_a').innerHTML = newOptions;
                }
            });
        });

        $('#id_model_c').change(function() {
            var b_ids = $('#id_model_b').val();
            var c_ids = $(this).val();
            var params = {
                'b': b_ids,
                'c': c_ids
            };

            $.ajax({
                url: '/retrieve_options/',
                data: params,
                dataType: 'json',
                success: function (data) {
                  var newOptions = '';
                  for (var i = 0; i < data.a_options.length; i++) {
                    newOptions += ('<option value="' +data.a_options[i][0]+ '">' +data.a_options[i][1]+ '</option>');
                  }
                  document.getElementById('id_model_a').innerHTML = newOptions;
                }
            });
        });
    });
})(django.jQuery);