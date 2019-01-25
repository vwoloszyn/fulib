# fulib
A simple crawler for searching for thesis and documents publicly available by Freie Universität.

```python
    import fulib
    q= fulib.query("fake news")
    print (q)
```


```javascript
[
  {
    'title': 'Fake news',
    'author': 'Anonymous',
    'link': 'https://fu-berlin.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=TN_proquest1876465797&context=PC&vid=FUB&lang=en_US&search_scope=FUB_ALL&adaptor=primo_central_multiple_fe&tab=fub&query=any,contains,fake%20news&offset=0',
    'publisher': 'Nature, Mar 9, 2017, Vol.543(7644), p.150'
  },
  {
    'title': 'Fayke newes : the media vs the mighty from Henry VIII to Donald Trump',
    'author': 'Derek J Taylor',
    'link': 'https://fu-berlin.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=FUB_ALMA_DS211003561170002883&context=L&vid=FUB&lang=en_US&search_scope=FUB_ALL&adaptor=Local%20Search%20Engine&tab=fub&query=any,contains,fake%20news&offset=0',
    'publisher': 'Stroud, Gloucestershire : The History Press, 2018'
  },
]
```



| **Argument**   | **Type**        | **Default**    | **Required?** |
|----------------|-----------------|----------------|---------------|
| `q`            | string          | `""`           | Yes           |
| `pages`        | int             | 1              | No            |
| `details`      | binary          | `False`        | No            |


