#!/usr/local/bin/WolframScript -script
L=Read[StringToStream[#],Number]&/@$ScriptCommandLine[[2;;]]
Fun[p1_, d1_, p2_, d2_] := (r = 6371.4;
  s[p_] := 
   r {Cos[p[[2]]] Cos[p[[1]]], Cos[p[[2]]] Sin[p[[1]]], Sin[p[[2]]]};
  d[pp1_, pp2_] := Norm[s[pp1*Pi/180.] - s[pp2*Pi/180.]];
  {{j, w} /. 
    FindRoot[{d[p1, {j, w}] == d1, 
      d[p2, {j, w}] == d2}, {{j, p1[[1]]}, {w, p2[[2]]}}], {j, w} /. 
    FindRoot[{d[p1, {j, w}] == d1, 
      d[p2, {j, w}] == d2}, {{j, p2[[1]]}, {w, p1[[2]]}}]})
Print[Fun[{L[[1]],L[[2]]},L[[3]],{L[[4]],L[[5]]},L[[6]]]]
