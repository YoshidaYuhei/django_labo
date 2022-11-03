# OR Mapper
## select
### 主キー名が何であれpkで取得できる
* obj = Model.objects.get(pk=1)

### where (複数件取得)
* objs = Model.objects.filter(name=name)

### where AND
* objs = Model.objects.filter(name=name, title=title)

### IN句
* objs = Model.objects.filter(key__in=['test1', 'test2'])

### where OR
* objs = Model.objects.filter(Q(name=name) | Q(title=title))

### 比較演算子
* objs = Model.objects.filter(weight__gt=2)
* objs = Model.objects.filter(weight__lt=2)
* objs = Model.objects.filter(weight__gte=2)
* objs = Model.objects.filter(weight__lte=2)

### between
* objs = Model.objects.filter(weight__range(1, 10))

### is_null
* objs = Model.objects.filter(key__isnull=True)

### LIKE句
* objs = Model.objects.filter(key__startswith="foo")
* objs = Model.objects.filter(key__contains="foo")
* objs = Model.objects.filter(key__endwith="foo")

### order_by
* objs = Model.objects.order_by("key")
* objs = Model.objects.order_by("-key")

### distinct
* objs = Model.objects.filter(key=value).distinct(key)

### dict, listで取得
* objs = Model.objects.values()
* objs = Model.objects.values_list("key", flat=True)

### count
* objs = Model.objects.filter(key=value).count()

### 最新、最古レコード
* objs = Model.objects.latest("created_at")
* objs = Model.objects.earliest("created_at")

### レコードの存在チェック
* if Model.objects.filter(key=value).exists():


## insert
### 通常
* obj = Model.objects.create(key=value)  
  obj.save()

### レコードがあれば取得、なければinsert
* obj = Model.objects.get_or_create(name=name, title=title, description=description)

## update
### 通常
* obj = Model.objects.get(key=value)
  obj.name = value
  obj.save()

### 悲観ロック
* objs = Model.objects.select_for_update().filter(key=value)

### レコードがあれば更新、なければinsert
* objs = Model.objects.update_or_create(name=name, title=title, description=description)

### 一括更新
* objs = Model.objects.filter(key=value)
  objs.update(name="foo")

# Model Type
* CharField(null=True, max_length=必須)
* TextField(null=True)
* IntegerField(default=0, db_index=True)
* ImageField(upload_to, height_field, width_field)
* JSONField(encoder, decorder)
* ManyToManyField(to)
* ForeignKey(to, on_delete=models.CASCADE,PROTECT,SET_NULL,SET_DEFAULT)
* IntegerChoices
* DateField(auto_now, auto_now_add)
  * auto_nowはModel.save()の度に更新される、auto_now_addはInsertされた時のみ更新される
  * auto_now、auto_now_addがTrueの場合、このフィールドに手動で日付を入れても無視される