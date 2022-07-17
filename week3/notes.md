Train data: 50_000
Test data: 10_000

## First iteration
```
N       10000
P@1     0.482
R@1     0.482

N       10000
P@3     0.215
R@3     0.644

N       10000
P@5     0.141
R@5     0.707
```

## With -lr 0.5 -epoch 25 -wordNgrams 2
```
N       10000
P@1     0.518
R@1     0.518

N       10000
P@3     0.234
R@3     0.703

N       10000
P@5     0.154
R@5     0.772
```

## With min_queries 10_000
```
N       10000
P@1     0.584
R@1     0.584

N       10000
P@3     0.262
R@3     0.785

N       10000
P@5     0.168
R@5     0.842
```

## Without stemming
```
N       10000
P@1     0.521
R@1     0.521

N       10000
P@3     0.235
R@3     0.704

N       10000
P@5     0.154
R@5     0.77
```


## Questions
1. For query classification:
    - How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?
        - **1000:** 387
        - **10_000:** 69
    - What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.
        Best values was with `stemming, -lr 0.5 -epoch 25 -wordNgrams 2 and min_queries 10_000`:
        ```
        N       10000
        P@1     0.584
        R@1     0.584

        N       10000
        P@3     0.262
        R@3     0.785

        N       10000
        P@5     0.168
        R@5     0.842
        ```

        Another interesting side is that `stemming` has low impact to results. Iteration `With -lr 0.5 -epoch 25 -wordNgrams 2` and `Without stemming` has almost the same results.
2. For integrating query classification with search:
    - Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.
        - `ps3` - if we increase minimum score then more catageries are included such as `PS3 consoles` and `PS3 games` which actually are quite accurate.
        - `remote controler` - all reviewed results was accurate.

    - Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.
        - `ps3` - with minimum score set to `0.5` there is downside that only `PS3 Consoles` category is recognized and no games was returned. If minimum score is increased to `0.7` then `PS3 Games` also returned
        - `Iphone` - if minimum score set to `0.6` or more then a lot of categories are taken in consideration and main category `mobile phones` are pushed down and can be missed easily
