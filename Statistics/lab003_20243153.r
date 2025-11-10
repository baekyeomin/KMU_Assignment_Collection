data = read.table("data.txt")
k = nrow(data)
print(k)

n = nrow(mtcars) - (k%%5)
print(n)

mt = mtcars[1:n,]

am0 = mt[mt$am == 0, "wt"]
mean_wt_am_0 = mean(am0)
stderr_wt_am_0 = sd(am0) / sqrt(length(am0))
conf_interval_am_0 = t.test(am0, conf.level = 0.99)$conf.int
attr(conf_interval_am_0, "conf.level") <- NULL  # conf.level 속성 제거
print(conf_interval_am_0)

# am 필드가 1인 차량의 wt 값 평균이 2.1보다 큰지 검정
am1 = mt[mt$am == 1, "wt"]
t_test_am_1 = t.test(am1, mu = 2.1, alternative = "greater")
print(t_test_am_1$p.value)

# 두 번째 열과 세 번째 열에 대한 대응표본 t-test와 신뢰구간
data2_3 = data[, c(2, 3)]  # 두 번째 열과 세 번째 열 추출

# 대응표본 t-test
paired_t_test = t.test(data2_3[, 1], data2_3[, 2], paired = TRUE, conf.level = 0.95)
attr(paired_t_test$conf.int, "conf.level") <- NULL  # conf.level 속성 제거
print(paired_t_test$conf.int)

# 독립표본 t-test
independent_t_test = t.test(data2_3[, 1], data2_3[, 2], paired = FALSE, conf.level = 0.95)
attr(independent_t_test$conf.int, "conf.level") <- NULL  # conf.level 속성 제거
print(independent_t_test$conf.int)
