margin = {
    top: 20,
    right: 50,
    bottom: 50,
    left: 80
};

width = 1000 - margin.left - margin.right;
height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .domain([0,24000])
    .range([0, width]); //X-Scale
var y = d3.scale.linear()
    .domain([0,8e+39])
    .range([height, 0]); //y-Scale

var line = d3.svg.line()
    .x(function (d) {
        return x(d.x);
    })
    .y(function (d) {
        return y(d.y);
    });

var zoom = d3.behavior.zoom()
    .x(x)
    .y(y)
    .on("zoom", function(){
        if(d3.event.sourceEvent.which!=3){
            refresh();
        }
    });
var zoomRect = true;
    svg = d3.select('.graph')
    .append("svg:svg")
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append("svg:g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    .call(zoom)
    .append("g")
    .on("mouseup", function(){
        d3.select('body').style("cursor", null);
    })
    .on("mousedown", function() {
        d3.select('body').style("cursor", "move");
        if (d3.event.which != 3) return;
        var e = this,
        origin = d3.mouse(e),
        rect = svg.append("rect").attr("class", "zoom");
        d3.select("body").classed("noselect", true);
        origin[0] = Math.max(0, Math.min(width, origin[0]));
        origin[1] = Math.max(0, Math.min(height, origin[1]));
        d3.select(window)
        .on("mousemove.zoomRect", function() {
            var m = d3.mouse(e);
            m[0] = Math.max(0, Math.min(width, m[0]));
            m[1] = Math.max(0, Math.min(height, m[1]));
            rect.attr("x", Math.min(origin[0], m[0]))
            .attr("y", Math.min(origin[1], m[1]))
            .attr("width", Math.abs(m[0] - origin[0]))
            .attr("height", Math.abs(m[1] - origin[1]));
        })
        .on("mouseup.zoomRect", function() {
            d3.select(window).on("mousemove.zoomRect", null).on("mouseup.zoomRect", null);
            d3.select("body").classed("noselect", false);
            var m = d3.mouse(e);
            m[0] = Math.max(0, Math.min(width, m[0]));
            m[1] = Math.max(0, Math.min(height, m[1]));
            if (m[0] !== origin[0] && m[1] !== origin[1]) {
                zoom.x(x.domain([origin[0], m[0]].map(x.invert).sort(function(a,b){return a > b;})))
                .y(y.domain([origin[1], m[1]].map(y.invert).sort(function(a,b){return a > b;})));
            }
            rect.remove();
            refresh();
        }, true);
        d3.event.stopPropagation();
    });

svg.append("svg:rect")
.attr("width", width)
.attr("height", height)
.attr("class", "plot");

$(document).ready(function(){
    getData(0,0,0);
});

var make_x_axis = function () {
    return d3.svg.axis()
    .scale(x)
    .orient("bottom");
};

var make_y_axis = function () {
    return d3.svg.axis()
    .scale(y)
    .orient("left");
};

var xAxis = d3.svg.axis()
.scale(x)
.orient("bottom");

svg.append("svg:g")
.attr("class", "x axis")
.attr("transform", "translate(0, " + height + ")")
.call(xAxis);

var yAxis = d3.svg.axis()
.scale(y)
.orient("left")
.tickFormat(function(d){
    return d.toExponential(1);
});

svg.append("g")
.attr("class", "y axis")
.call(yAxis);

svg.append("g")
.attr("class", "x grid")
.attr("transform", "translate(0," + height + ")")
.call(make_x_axis()
    .tickSize(-height, 0, 0)
    .tickFormat(""));

svg.append("g")
.attr("class", "y grid")
.call(make_y_axis()
    .tickSize(-width, 0, 0)
    .tickFormat(""));

var clip = svg.append("svg:clipPath")
.attr("id", "clip")
.append("svg:rect")
.attr("x", 0)
.attr("y", 0)
.attr("width", width)
.attr("height", height);

var chartBody = svg.append("g")
.attr("clip-path", "url(#clip)");

var circlesLayer = chartBody.append("g")
.attr("id","circles")

svg.append("text")
.attr("class","labels")
.attr("text-anchor","end")
.attr("x",width / 2)
.attr("y",height + 40)
.text("Wavelength (Å)")

svg.append("text")
.attr("class","labels")
.attr("text-anchor","end")
.attr("x", -height/2 + margin.bottom)
.attr("y", -75)
.attr("dy","0.75em")
.attr("transform","rotate(-90)")
.text("Luminosity (lux)")

var legendBox = svg.append("g")
.attr("id","legend")
.attr('display','none')

legendBox.append("rect")
.attr("width",155)
.attr("height",70)
.attr("x",width - 175)
.attr("y",25)
.attr("fill","lightgray")
.attr("stroke","black")

legendBox.append("rect")
.attr("width",15)
.attr("height",15)
.attr("x",width - 165)
.attr("y",35)
.attr("fill","green")
.attr("stroke","black")

legendBox.append("text")
.attr("x",width - 145)
.attr("y",47)
.text("Overplotted Graph")
.attr("class", "legendtext")

legendBox.append("rect")
.attr("width",15)
.attr("height",15)
.attr("x",width - 165)
.attr("y",65)
.attr("fill","steelblue")
.attr("stroke","black")

legendBox.append("text")
.attr("x",width - 145)
.attr("y",77)
.text("Simulated Graph")
.attr("class", "legendtext")


function graphData(data){
    if(clearData){
        chartBody.selectAll(".line").remove();
    }
    chartBody.append("svg:path")
    .datum(data)
    .attr("class", "line")
    .attr("d", line);
    refresh();   
}

function graphOverplot(data){
    if(clearData){
        chartBody.selectAll(".overplot").remove();
    }
    chartBody.append("svg:path")
    .datum(data)
    .attr("class", "overplot")
    .attr("d", line);
    refresh();
}

var circleshidden = false;

function refresh() {
    svg.select(".x.axis").call(xAxis);
    svg.select(".y.axis").call(yAxis);
    svg.select(".x.grid")
    .call(make_x_axis()
        .tickSize(-height, 0, 0)
        .tickFormat(""));
    svg.select(".y.grid")
    .call(make_y_axis()
        .tickSize(-width, 0, 0)
        .tickFormat(""));
    svg.selectAll(".line")
    .attr("class", "line")
    .attr("d", line);
    svg.selectAll(".overplot")
    .attr("class", "overplot")
    .attr("d", line);
    if(zoom.scale() > 10 && !circleshidden){
        showCircles();
        resetMouseListeners();
    } else{
        d3.selectAll("circle").remove();
    }
}

function restoreScale(){
    zoom.x(x.domain(d3.extent(frameData[currTime][currMu][currPhi], function (d) {
        return d.x;
    }))
    .range([0, width]))
    .y(y.domain(d3.extent(frameData[currTime][currMu][currPhi], function (d) {
        return d.y;
    }))
    .range([height, 0]));
    refresh();
}

function showCircles(){
    var circles = circlesLayer.selectAll("circle")
    .data(frameData[currTime][currMu][currPhi]);

    circles.enter()
    .append("circle")
    .attr("r",3)
    .attr("stroke","black")
    .attr("stroke-width","1px")
    .attr("fill","teal")
    .attr("cx",function(d){
        return x(d.x);
    })
    .attr("cy",function(d){
        return y(d.y);
    });

    circles.attr("cx",function(d){
        return x(d.x);
    })
    .attr("cy",function(d){
        return y(d.y);
    });
}


var currTime = 0;
var currMu = 0;
var currPhi = 0;
var frameData = [];
var clearData = true;
var animation;
var rescale = false;

function runAnimation(start, end, speed){
    if(animation){
        animation = clearInterval(animation);
    }
    animation = setInterval(getNextFrame, speed);
}

function getNextFrame(){
    moveFrame(1, 0, 0);
}

function preloadData(method, step, step2){
    $(".graph").append("<div id='loadingscreen'><img width='32px' height='32px' src='/site_media/odetta/img/loader.gif'/></div>");
    $(".btn").attr("disabled",true);
    $(".nav-list li").attr("class","disabled");
    d3.json("/odetta/ajax/"+method+"/"+m_id+"/"+step+"/" + step2 + "/", function(error, data){
        if (error){
            console.log(error);
        }else{
            for(var index in data){
                var d = data[index];
                if(frameData[d.time_step] == undefined){
                    frameData[d.time_step] = [];
                }
                if(frameData[d.time_step][d.mu_step] == undefined){
                    frameData[d.time_step][d.mu_step] = [];
                }
                if(frameData[d.time_step][d.mu_step][d.phi_step] == undefined){
                    frameData[d.time_step][d.mu_step][d.phi_step] = d.flux_data;
                }
                
            }
        }
        $(".nav-list li").removeClass("disabled");
        $(".btn").attr("disabled",false);
        $("#loadingscreen").remove();
    });
}

function moveFrame(time, mu, phi){
    currTime+=parseInt(time);
    if(currTime < 0){
        currTime = 0;
    }
    currMu+=parseInt(mu);
    if(currMu < 0){
        currMu = 0;
    }
    currPhi+=parseInt(mu);
    if(currPhi < 0){
        currPhi = 0;
    }
    $("#time-slider").slider("option", "value", currTime);
    $("#mu-slider").slider("option", "value", currMu);
    $("#phi-slider").slider("option", "value", currPhi);
}

function getData(time, mu, phi){
    if(frameData[time]&&frameData[time][mu]&&frameData[time][mu][phi]){
        graphData(frameData[time][mu][phi]);
        currTime = parseInt(time);
        currMu = parseInt(mu);
        currPhi = parseInt(phi)
        if(rescale){
            restoreScale();
        }
    }else{
        d3.json("/odetta/ajax/plot/"+m_id+"/"+time+"/"+mu+"/"+phi+"/", function(error, data){
            if (error || data.success == false){
                if(error){
                    console.log(error);
                }
                console.log(data);
                console.log(data.error);
                if(animation){
                    animation = clearInterval(animation);
                }
            }else{
                frameData[data.time_step] = [];
                frameData[data.time_step][data.mu_step] = [];
                frameData[data.time_step][data.mu_step][data.phi_step] = data.flux_data;
                graphData(data.flux_data);
                currTime = parseInt(data.time_step);
                currMu = parseInt(data.mu_step);
                currPhi = parseInt(data.phi_step);
                if(rescale){
                    restoreScale();
                }
            }
        });
    }
}

function getPlot(time,mu,phi){
    d3.json("/odetta/ajax/plot/"+m_id+"/"+time+"/"+mu+"/"+phi+"/", function(error, data){
        if (error || data.success == false){
            if(error){
                console.log(error);
            }
            console.log(data);
            console.log(data.error);
            if(animation){
                animation = clearInterval(animation);
            }
        }else{
            frameData[data.time_step] = [];
            frameData[data.time_step][data.mu_step] = [];
            frameData[data.time_step][data.mu_step][data.phi_step] = data.flux_data;
            graphData(data.flux_data);
            currTime = parseInt(data.time_step);
            currMu = parseInt(data.mu_step);
            currPhi = parseInt(data.phi_step);
            if(rescale){
                restoreScale();
            }
        }
    });
}

function resetMouseListeners(){
    d3.selectAll("circle").on("mouseover",null);
    d3.selectAll("circle").on("mouseout",null);
    d3.selectAll("circle")
        .on("mouseover",function(d){
            d3.select(this)
                .transition()
                .duration(500)
                .attr("opacity",0.75)
                .attr("r", 5);

            svg.append("text")
                .attr("opacity",0)
                .transition()
                .duration(500)
                .text("Wavelength:" + Math.floor((d.x)) + " Å")
                .attr("x",function(){
                    return x(d.x) + 10;
                })
                .attr("y", function(){
                    return y(d.y) + 5;
                })
                .attr("fill","black")
                .attr("font-family","sans-serif")
                .attr("font-size",12)
                .attr("class","info")
                .attr("opacity",1.0);
            svg.append("text")
                .attr("opacity",0)
                .transition()
                .duration(500)
                .text("Luminosity:" + Math.floor((d.y)) + " lux")
                .attr("x",function(){
                    return x(d.x) + 10;
                })
                .attr("y", function(){
                    return y(d.y) + 25;
                })
                .attr("fill","black")
                .attr("font-family","sans-serif")
                .attr("font-size",12)
                .attr("class","info")
                .attr("opacity",1.0);
        })
        .on("mouseout",function(d){
            d3.select(this)
                .transition()
                .duration(400)
                .attr("opacity",1)
                .attr("r",3);
            svg.selectAll(".info")
                .transition()
                .duration(250)
                .remove();
        });
}
function hideShow(graph_name){
    if($("." + graph_name).attr("display") != 'none'){
        $("." + graph_name).attr("display","none");
        $("." +graph_name + "Btn").html("Show " + graph_name);
        if(graph_name == "line" && zoom.scale() > 10){
            circlesLayer.selectAll("circle").remove();
            circleshidden = true;
        }
        $("#legend").attr("display","none");
    }
    else{
        $("." + graph_name).attr("display","inline");
        $("." + graph_name + "Btn").html("Hide " + graph_name);
        if(zoom.scale() > 10){
            showCircles();
            circleshidden = false;
            resetMouseListeners();
        }
        $("#legend").attr("display","inline");
    }
}