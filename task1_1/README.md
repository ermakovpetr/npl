Task:  __Find total payouts by countries__

Structure log file
```
ip, userid, country, bannerid, payout
```

Log:
```
29.32.144.161, f9e4abc5a446586e575266e9f2b81b80, Costa Rica, 372332b350eaa7dfed552ec40219cd7d, 0.29
174.109.164.213, f1da63dd30ca5181a6194af92b36b48f, Australia, 3c00efcb57f0fe320792692eca2da708, 0.15
86.58.216.110, ab2b0b3e31a14576f050ee36f80f131e, United Arab Emirates, 9d81ed0440ae8767c585d97f744f6c33, 0.69
3.216.52.63, 44f3d9e942b758f2a8110088ccbfc3fd, Iceland, c2ac946069b0bb4e1512bee9d4c46c75, 0.70
133.93.85.111, d73c4ea9658b36ba20ea139af7232eda, Luxembourg, 862b0ae7b20ba19f2634c23edf7c50bf, 0.39
190.189.223.112, 25a198fc4ad82da503c4cd3c8fc445c3, Luxembourg, 87ccc78c0aa705a8f43295a0a813505a, 0.32
57.147.10.224, 7452cf65b10ba0f98ee8b0cfef94b045, Mexico, 49bcabe27b8dc8da9405a729f231c5f3, 0.20
142.218.75.89, a255a2cdb5d095f2650845b3daab162c, Venezuela, 510f1858f570e6b677413050658b7665, 0.49
83.8.233.93, ef096a715708b62168d6554807bff17a, Panama, bfe0e43f5072729f10d44b6650e7316a, 0.22
205.193.117.8, c4aa4c1153796ceda9a328af0379459b, United Kingdom, 7bf109335038ba76381691a8bb2ae8d8, 0.33
0.153.59.119, 84d0c3a17b34a09a971335d0146143d4, Belgium, ebb6613e657ef7c6cde9932a82581d65, 0.35
130.106.115.62, ab871bea79017937eb7caa2e8c0d3b13, Mexico, 1ba5531138dff5691beff2a9e16f0ffa, 0.10
174.52.50.120, 63a83ddb171848680377b5bc9416259c, Venezuela, 0cccfd7c37fe7361bc248c701307f894, 0.25
9.68.83.143, a5ae6ee647d9b3df3a9a37a9fd309ce4, Luxembourg, 60f46b459ea9c4bc4737947c9d3a7528, 0.34
91.146.199.184, 0dcac7647e30dc5c734bf6950e2b1673, Panama, d31b9e5eecf1a761f8d679d1065d12b0, 0.35
37.115.124.167, f64c1f40de99594f8a6642cf30e9fc3e, Luxembourg, 48c343ab207e5d95e313d40679a176ea, 0.47
51.36.186.46, a9bbd01edecde6560e1d2eb29b78deec, United Arab Emirates, b9a805c948839b1a297b55381042be91, 0.86
105.218.52.83, b009b01d4d8db182625e44f5b66ca025, United Arab Emirates, b9db3ef7c0522c61f76e464c34c79f46, 0.71
245.229.85.27, 188d8985bcab3f8bc2e31ef5e3ab3dc7, Luxembourg, bf1eabcb92f5830480c5851182600d2c, 0.26
255.169.47.10, f09daf39fd88ba451b6782a622fcfbc1, Austria, 4bbe36aff95b928258ce264cada9315f, 0.26
```

Command for start
```bash
hadoop jar hadoop-streaming.jar \
    -input /users/advert_input \
    -output /users/advert \
    -mapper map.py \
    -reducer reduce.py \
    -file map.py \
    -file reduce.py
```
