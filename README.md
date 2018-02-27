# BloomFilter

 
布隆过滤器基于位图，redis有bitmap这种数据结构（bitmap是基于string的）最大可有512M（2的32次方个位）
有以下特点
 * 非常高效
 * 只能增加不能删除、
 * 会误报，但是不会漏掉
