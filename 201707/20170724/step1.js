//for(var i=Date.parse('2016-02-27');i<=Date.parse('2017-03-01');i+=86400000)console.info(new Date(i))

for (var o = i.period.split("|")[0], r = o.substring(0, 4), u = o.substring(4, 6), l = o.substring(6, 8),
         d = new Date(r + "/" + u + "/" + l).getTime(), M = 0; M < e.day; M++) {
    var p = new Date(d + 24 * M * 60 * 60 * 1e3);
    a.push(L.a.formatDate(p, "MM/dd"))
}

