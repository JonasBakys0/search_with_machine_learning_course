# Level 1

## Stemmed data set results
```
N       9678
P@1     0.63
R@1     0.63
```

## Pruned data set results
```
N       10000
P@1     0.97
R@1     0.97
```

# Level 2

## Candidate synonyms with original titles
- **Query word? iphone:**
```
Saxophone 0.852884
Speakerphone 0.84585
Microphone 0.834952
Earphones 0.819387
Telephone 0.818783
Ozone 0.792074
Telephones 0.788825
Headphone 0.781387
Phone 0.775247
Jawbone 0.77213
```
- **Query word? iPhone:**
```
iPhone®, 0.955711
iPhone® 0.940529
iPod®/iPhone 0.830524
iPod®/iPhone® 0.814395
3GS, 0.79807
3G, 0.792445
3G/3GS 0.787894
4S 0.78672
3GS 0.778476
4/4S 0.775185
```

## Candidate synonyms with normalized titles
- **Query word? iphone:**
```
4s 0.839458
apple 0.802414
ozone 0.769493
3gs 0.752483
ifrogz 0.747663
ipod 0.725857
amethyst 0.723724
ipadÂ 0.719229
ipodÂ 0.714934
appleÂ 0.709781
```
- **Query word? iPhone:**
```
hone 0.924557
phone 0.84665
ozone 0.826154
gophone 0.823776
iphone 0.777297
saxophone 0.765268
speakerphone 0.760594
jawbone 0.757146
bone 0.751268
cone 0.708898
```
- **headphones:**
```
headphone 0.938304
earbud 0.898094
ear 0.851783
earphones 0.824314
bud 0.782632
behind 0.750109
earbuds 0.747855
earloomz 0.736868
sennheiser 0.730029
gumy 0.72483
```
- **ps2:**
```
ps3 0.880788
2k7 0.824761
2k3 0.821643
2k5 0.820547
2k8 0.81887
nhl 0.81738
2k9 0.812175
2k6 0.811918
psp 0.807184
wwe 0.806478
```

## Candidate synonyms with stemmed titles
- **Query word? iphone:**
```
iphone®, 0.943094
iphone® 0.926151
iphon 0.854739
ipod®/iphone 0.853122
ipod®/iphone® 0.822487
4s 0.788687
3gs 0.78008
ipod®, 0.766272
3g/3gs 0.764307
3g/3g 0.759891
```
- **Query word? iPhone:**
```
hone 0.938431
gophone 0.846141
phone 0.839473
ozone 0.82916
saxophone 0.811448
4-zone 0.788598
iphone 0.764191
speakerphone 0.763797
v-tone 0.746628
zone 0.736206
```

## With epochs 25 and minCount 20
- **Query word? iphone:**
```
4s 0.889875
apple 0.805177
ipod 0.767414
3gs 0.727607
ipad 0.700223
4th 0.606972
mophie 0.558793
earbud 0.547958
generation 0.541832
ifrogz 0.540911
```
- **Query word? iPhone:**
```
phone 0.745999
telephone 0.742725
speakerphone 0.697656
waiting 0.690361
answering 0.679255
headphone 0.659498
handset 0.650495
dect 0.627911
caller 0.62487
corded 0.62344
```
- **headphones:**
```
earbud 0.906333
ear 0.854892
headphone 0.833339
earphones 0.678171
bud 0.675129
2xl 0.672805
lowrider 0.671918
over 0.656067
earbuds 0.626453
fidelity 0.626346
```
- **ps2:**
```
xbox 0.738867
ps3 0.738041
gba 0.728583
360 0.714537
gamecube 0.711748
psp 0.682248
guide 0.664192
cheats 0.636772
boy 0.629217
```

Using model with epochs 25 and minCount 20. From couple tests I pick **0.70** treshold score.

# Level 3

Seems kinda bad synonyms that I have with this model. For example with `earbuds`, `nespresso` and `dslr` have no impact same `total_hit_count`. 
`earbuds` have some strange synonyms like `gumy, buds, aerosport, iclear,` and there was no `nespresso` at all. But for some words it worked like `nintendo`, 
- **nintendo without synonyms:**
```
"hits": {
    "total": {
      "value": 4568,
      "relation": "eq"
    },
```

- **nintendo with synonyms:**
```
...
  "hits": {
    "total": {
      "value": 6457,
      "relation": "eq"
    },
    ...
``` 

Overall my synonyms were quite bad. Need to return to the synonyms generation step and try different model.
