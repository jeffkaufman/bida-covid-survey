from collections import Counter

attendances = {
    "Every time": 20,
    "About monthly": 10,
    "Just started going": 10,
    "Just moved back to the area, plan to attend about monthly.": 10,
    "I was previously attending every time. Now I'm on a new routine and "
    "haven't figured out how frequently I'm attending.": 10,
    "Given BIDA's current policies and the current case counts, I'm planning "
    "to start attending regularly again after a hiatus due to COVID, but if "
    "BIDA's policies relaxed or case counts went up, I wouldn't be able to "
    "come." : 8,
    "More than monthly, not quite every time. ": 7, 
    "About quarterly": 4,
    "I was waiting until I got bivalent booster to start attending again. "
    "Will start attending again in December.": 4,
    "I will start attending when I move back to Boston at the end of the "
    "year.": 4,
    "Occasionally ": 2,
    "Only once since pandemic, but hoping to start attending more "
    "frequently.": 2,
    "About yearly": 1,
    "I don't currently attend, but have been thinking about starting up.": 1,
    "I haven't attended since the pandemic but am interested in returning ": 1,
    "Considering beantown stomp": 1,
    "I haven't been attending, but it's a very close call and I have been "
    "very close to deciding I'm comfortable going": 1,
    "Haven't attended in over a year, but planning to": 1,
    "I don't attend, but I would if you had different covid policies": -1,
    "I don't attend but I might if you had different covid policies": -1,
    "I don’t attend but having you check for vaccinations and cap the amount "
    "of dancers would change my mind ": -1,
    "There are a couple of other impediments to me attending, one of them "
    "hopefully temporary, but the covid policy doesn't entirely work "
    "for me.": -1,
    "I don't attend, and there isn't currently anything that would make "
    "me comfortable attending": -2
}

changes = {
    "Required bivalent boosters": "bivalent",
    "Stopped requiring masks": "nomask",
    "Stopped requiring masks without requiring testing instead": "nomask",
    "Allowed testing instead of masking": "test-nomask",
    "Allowed testing instead of vaccination": "test-novax",
    "Stopped requiring vaccination": "novax",
    "Made more exceptions": "except",
    "Stopped requiring boosters": "noboost",
    "Allowed for lesser grade masks": "surgical",
    "Allowed the blue surgical masks instead of N95/KN95. My glasses fog up "
    "and it’s hard to see .": "surgical",
    "a surgical mask should be fine": "surgical",
    "Stopped requiring N95 and allowing surgical masks instead": "surgical",
    "Stopped requiring high filtration masks": "surgical",
    "Would prefer to wear surgical masks rather than heavy duty ones because "
    "it seems like the middle ground for those of us who are vaxed": "surgical",

}

more_counts = Counter()
less_counts = Counter()

more_counts_w = Counter()
less_counts_w = Counter()

with open("responses.tsv") as inf:
    for line in inf:
        if not line.strip(): continue
        line = line.removesuffix("\n")

        (response_number, timestamp, attendance,
         increase, decrease,
         comments_a, comments_b) = line.split("\t")

        if response_number == "Response": continue

        attendance = attendances[attendance]

        for change in increase.split(", "):
            if change in changes:
                more_counts[changes[change]] += 1
                more_counts_w[changes[change]] += max(attendance, 0)
        for change in decrease.split(", "):
            if change in changes:
                less_counts[changes[change]] += 1
                less_counts_w[changes[change]] += max(attendance, 0)

        if False:
            for x in [comments_a, comments_b]:
                if x:
                    print("<li>%s</li>" % (x))

if False:
    print("change\tincrease\tdecrease")
    for change in sorted(set(changes.values())):
        print("%s\t%s\t%s" % (
            change, more_counts[change], less_counts[change]))
if False:
    print("change\tincrease\tdecrease")
    for change in sorted(set(changes.values())):
        print("%s\t%s\t%s" % (
            change, more_counts_w[change], less_counts_w[change]))
