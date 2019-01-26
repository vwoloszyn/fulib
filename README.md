# fulib
A simple crawler for searching for thesis and documents publicly available by Freie Universität.

```python
    import fulib
    q= fulib.query("fake news")
    print (q)
```

output:
```javascript
[
  {
    'title': 'Fake news',
    'author': 'Anonymous',
    'link': 'https://fu-berlin.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=TN_proquest1876465797&context=PC&vid=FUB&lang=en_US&search_scope=FUB_ALL&adaptor=primo_central_multiple_fe&tab=fub&query=any,contains,fake%20news&offset=0',
    'publisher': '',
    'Title': 'Fake news',
    'Author': 'Anonymous',
    'Is Part Of': 'Nature, Mar 9, 2017, Vol.543(7644), p.150',
    'Description': 'There has been much gnashing of teeth in the science-journalism community this week, with the release of an infographic that claims to rate the best and worst sites for scientific news. According to the American Council on Science and Health, which helped to prepare the ranking, the field is in a shoddy state. "If journalism as a whole is bad (and it is)," says the council, "science journalism is even worse. Not only is it susceptible to the same sorts of biases that afflict regular journalism, but it is uniquely vulnerable to outrageous sensationalism" (see go.nature.com/2mhmupd).',
    'Identifier': 'ISSN: 00280836',
    'Language': 'English',
    'Subjects': 'Journalism\nScience',
    'Source': '© ProQuest LLC All rights reserved\nSHOW COLLECTIONS'
  },
 ]
```



| **Argument**   | **Type**        | **Default**    | **Required?** |
|----------------|-----------------|----------------|---------------|
| `q`            | string          | `""`           | Yes           |
| `pages`        | int             | 1              | No            |
| `details`      | binary          | `False`        | No            |





