$('#selected_month').change(function() {
    var month = $(this).val();
    var days_of_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    var monthNames = ['January ', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    var dayNamesMin = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'];
    dayNames = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];
    var day = new Date();
    day.setMonth(month);
    var mes = day.getMonth();
    var weekDay = new Date((monthNames[mes - 1]) + '01, 2019');
    for (i in monthNames) {
        if (i == month) {
            var table = '';
            var table2 = '';
            var table3 = '';
            var x = 1;
            var days = 0;
            var days_off = 0;
            var y = dayNames.indexOf(String(dayNames[weekDay.getDay()]));
            $("#weekDay").html(dayNames[y])
            console.log(dayNames[y])
            while (x <= (days_of_Month[month - 1])) {
                days++;
                days_off++;
                table += '<td>' + x + '</td>';
                table2 += '<td>' + dayNamesMin[y] + '</td>'
                x++;
                y++;
                if (y == 7) {
                    y = 0;
                }
                if (days_off == 7) {
                    //console.log(days);
                    days_off = 1;
                }

            }
            $(".days_of_month").html(table).addClass("table-bordered");
            $(".days_of_week").html(table2).addClass("table-bordered");
            $(".days_of_month").html(table[day]).css("background", "red");
        }

    }
});

var semana = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"];
var mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
var d = new Date();

document.getElementById("week").innerHTML = semana[d.getDay()];
document.getElementById("selected_month").value = (d.getMonth() + 1);
console.log(mes[d.getMonth()]);