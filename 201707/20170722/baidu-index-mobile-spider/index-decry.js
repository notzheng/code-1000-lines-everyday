/**
 * Created by JianJian on 2017/7/21.
 */


var u = {
    "status": 0,
    "uniqid": "597216992f7981.54848548",
    "data": [{
        "key": "\u643a\u7a0b",
        "index": [{
            "period": "20170422|20170720",
            "_all": "x0yYhyNe3zHRzhze3x3hNzxe3NzH0zRe3yh030xe3yhhyR0e33hxxxH",
            "_pc": "3HxN30e3Yhh33eNHxNhheNY3y03eNhzh3yeyzN3HyeNyRYN3",
            "_wise": "xHhHYxHexR0RxY0exRRRhz3exhyNN3He3xzRNHRe3zhY33yexhyNy0N"
        }]
    }]
};
var l = "xYNLyR0ie3zHCvh163+478%,205-.9";

// a = u.data[0].index[0]._all.split("")
M = l.split("");
p = {};
//构造字典，前半部分作为键，后半部分作为值，一一对应
for (v = 0; v < M.length / 2; v++) {
    p[M[v]] = M[M.length / 2 + v];
}

console.log(p);

//for (g = 0; g < u.data.length; g++) {
f = u.data[0].index[0]._all.split("");
h = u.data[0].index[0]._pc.split("");
m = u.data[0].index[0]._wise.split("");
w = [];
I = [];
y = [];

for (j = 0; j < f.length; j++) {
    w.push(p[f[j]]);
    I.push(p[h[j]]);
    y.push(p[m[j]]);
}

u.data[0].index[0].all = w.join("");
u.data[0].index[0].pc = I.join("");
u.data[0].index[0].wise = y.join("");
//
console.log(u.data[0].index[0]);

