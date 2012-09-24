/*
 * Things should eventually make their way into the jquery/d3-like
 * monolithic function/object. This is probably accepted js practice.
 */

var layout = (function() {
    return {
        layout: function () {
            $('div.layout');
        },
    }
});

var chartid_counter = -1;

function new_chartid () {
    chartid_counter += 1;
    return chartid_counter;
};

function show_controls (controls) {
    $(controls).children().not('svg').show();
}

function hide_controls (controls) {
    $(controls).children().not('svg').hide();
}

function getattr (obj, attr, def) {
    return (obj.hasOwnProperty(attr)) ? obj[attr] : def;
}

function add_chart (opts) {
    // if opts is not provided, make a dummy object
    opts = (typeof opts === "undefined") ? {} :  opts;

    id = new_chartid();

    d3.select('div.layout').append('div')
        .attr('class', 'controls')
        .attr('id', 'controls_' + id)
        .style('background-color', 'steelblue')  // debugging
        .style('position', 'absolute')
        .style('height', getattr(opts, "height", '100px'))
        .style('width', getattr(opts, "width", '100px'))
        .style('left', getattr(opts, "left", '0px'))
        .style('top', getattr(opts, "top", '0px'));

    controls = $('#controls_' + id);
    controls.resizable();
    controls.draggable();

    // add close button
    controls.append("<button>Close</button>");
    button = $('#controls_' + id + ' button');
    button.css('width', '15px')
        .css('height', '15px')
        .css('float', 'right');
    button.button({
            icons: {
                primary: "ui-icon-close"
            },
            text: false,
        }).click(function () {
            // this.parentElement = #controls_<i>
            this.parentElement.parentElement.removeChild(this.parentElement);
        });

    hide_controls(controls);

    d3.select('#controls_' + id)
        .on('mouseover', function () {
            show_controls(this);
        })
        .on('mouseout', function () {
            hide_controls(this);
        })
        .append('svg')
            .attr('class', 'chart')
            .attr('id', 'chart_' + id);
}

$().ready(function () {
    // bind right click
    $('div.layout').bind("contextmenu", function (event) {
        add_chart({"left": event.offsetX + 'px', "top": event.offsetY + 'px'});
        return false;
    });
});
