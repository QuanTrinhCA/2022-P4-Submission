# [Problem D: Geyser Field](https://nbhspc22.kattis.com/contests/nbhspc22/problems/nbhspc22.geyserfield)

On Earth, a geyser is a geological feature that briefly and energetically throws out steam and hot water on a somewhat periodic basis. The Old Faithful geyser is particularly famous.

Our national space agency has a probe orbiting one of Neptune’s moons, and it has detected a lot of geyser activity. On this moon, isolated geysers all are very regular. If a geyser erupts at time t1 and next at time t1 + a, it will definitely erupt the next times at t1 + 2a, t1 + 3a, and so forth. On earth, a geyser eruption can last several minutes, but on the Neptunian moons, eruptions are almost instantaneous.

There is one area that was initially mysterious, because it seemed to have a geyser that erupted irregularly. However, the geologists have decided that we actually have a small number (at most 20) of very regular geysers close together, as part of a “geyser field”. From orbit, we cannot distinguish between the different geysers in the field.

They’ve provided you with a recent history of geyser activity in this geyser field. They want to focus on the first geyser in this history, which they call Young Faithful, and they need you to predict the earliest that Young Faithful could erupt again. They hope that the history they have given you is long enough that Young Faithful will have erupted several times, but they state that that they cannot be sure.

The geologists believe that

- only Young Faithful was erupting at the first time, but for later measurements, it is possible that several geysers might be erupting simultaneously.

- the set of geysers has been unchanged for many years, so no new geyser is going to start erupting for the first time (or stop erupting) during the time period when measurements were taken.

- no geyser takes longer than 100000 time units between eruptions.

## Input
The first line of the input is a positive integer N, with N <= 1000 and N >= 2. Following this, we have N lines, each containing a positive integer, representing the times when there is geyser activity in the field. The N time measurements are given in ascending order, and the values never exceed 1000000. We assume that the first of these N measurements represents the eruption of only Young Faithful.

## Output
The output should be an integer that indicates the earliest time that Young Faithful could erupt again, in the future. (The answer must be larger than the most recent input time.)

In the first sample data, Young Faithful could have erupted at times 10 and 24, in which case the next eruption would be expected at 38.

## Sample Input 1
```
6
10
20
24
26
30
32
```

## Sample Output 1
```
38
```

## Sample Input 2
```
14
1000
1010
1011
1015
1020
1022
1028
1030
1035
1040
1041
1047
1060
1077
```

## Sample Output 2
```
1080
```
