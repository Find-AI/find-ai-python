# Changelog

## 1.3.0 (2025-05-16)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/Find-AI/find-ai-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** manual updates ([#23](https://github.com/Find-AI/find-ai-python/issues/23)) ([ef35843](https://github.com/Find-AI/find-ai-python/commit/ef35843af86df409a07ed8ed8c5869c63fb14e9c))
* **api:** manual updates ([#24](https://github.com/Find-AI/find-ai-python/issues/24)) ([c0f093f](https://github.com/Find-AI/find-ai-python/commit/c0f093fa9809ceff333e07f6cc57112c5fe2ad32))


### Bug Fixes

* **ci:** ensure pip is always available ([#42](https://github.com/Find-AI/find-ai-python/issues/42)) ([9497888](https://github.com/Find-AI/find-ai-python/commit/94978883bae3968267f40206af03e74fff1f624d))
* **ci:** remove publishing patch ([#43](https://github.com/Find-AI/find-ai-python/issues/43)) ([736f0c1](https://github.com/Find-AI/find-ai-python/commit/736f0c10fcb73ae7d9fd7e8166ad770bd46ece86))
* **client:** avoid OverflowError with very large retry counts ([#20](https://github.com/Find-AI/find-ai-python/issues/20)) ([7864786](https://github.com/Find-AI/find-ai-python/commit/78647867531c1dacaab324e228d87048c80f93fb))
* **client:** compat with new httpx 0.28.0 release ([#33](https://github.com/Find-AI/find-ai-python/issues/33)) ([ca61cd2](https://github.com/Find-AI/find-ai-python/commit/ca61cd2953ac090de4c950874724fd128d2ac73a))
* **package:** support direct resource imports ([cc7c769](https://github.com/Find-AI/find-ai-python/commit/cc7c7694bca53e8cb590ca44e1d90bbc3b37eeb6))
* **perf:** optimize some hot paths ([57017ce](https://github.com/Find-AI/find-ai-python/commit/57017ce439e8fd6340cd0b35c76f5660e076a0cb))
* **perf:** skip traversing types for NotGiven values ([339e929](https://github.com/Find-AI/find-ai-python/commit/339e929f1faa0e9dcb718dc51280bb0f1957bf22))
* **pydantic v1:** more robust ModelField.annotation check ([64f3d7b](https://github.com/Find-AI/find-ai-python/commit/64f3d7bb73b56126a6c257dca0a0b08466b943b9))
* **types:** handle more discriminated union shapes ([#41](https://github.com/Find-AI/find-ai-python/issues/41)) ([661cac7](https://github.com/Find-AI/find-ai-python/commit/661cac7d7503596cd57aaa30cb7b807836aabaaa))


### Chores

* add repr to PageInfo class ([#22](https://github.com/Find-AI/find-ai-python/issues/22)) ([6472a2f](https://github.com/Find-AI/find-ai-python/commit/6472a2f1f9379b905bcc7f7d70eb2a3da088d09f))
* broadly detect json family of content-type headers ([0843d9d](https://github.com/Find-AI/find-ai-python/commit/0843d9da078205d28433e574f4623a2b22f229fa))
* **ci:** add timeout thresholds for CI jobs ([dafadc6](https://github.com/Find-AI/find-ai-python/commit/dafadc664d30b6725ac2d943be23586128f81697))
* **ci:** fix installation instructions ([0b02f43](https://github.com/Find-AI/find-ai-python/commit/0b02f43f328dd93cfe8190e137f3fa74d2b2f55e))
* **ci:** only use depot for staging repos ([10b432d](https://github.com/Find-AI/find-ai-python/commit/10b432d62df01b5fbf7b40507ce180c7f3dc62f9))
* **ci:** upload sdks to package manager ([6b9b061](https://github.com/Find-AI/find-ai-python/commit/6b9b0614a17ffa1fbda8e6c090ae11b3f1899bbb))
* **client:** minor internal fixes ([ff34956](https://github.com/Find-AI/find-ai-python/commit/ff34956566f558c2656970b17eee48647b41e889))
* fix typos ([#44](https://github.com/Find-AI/find-ai-python/issues/44)) ([7ed0d63](https://github.com/Find-AI/find-ai-python/commit/7ed0d636f134b76225e8a0c0610486859eee59e7))
* **internal:** avoid errors for isinstance checks on proxies ([202ffd5](https://github.com/Find-AI/find-ai-python/commit/202ffd539c9c0ef14b12b42041a5ca64f36974a3))
* **internal:** base client updates ([5bf9b32](https://github.com/Find-AI/find-ai-python/commit/5bf9b322d236aa4fa7a6c3138470c194fed8f9f4))
* **internal:** bump pyright ([#34](https://github.com/Find-AI/find-ai-python/issues/34)) ([0364220](https://github.com/Find-AI/find-ai-python/commit/0364220b2d9b7de53b7d382a0ea03adf77c7f87b))
* **internal:** bump pyright version ([8d7d81b](https://github.com/Find-AI/find-ai-python/commit/8d7d81b697b58dbd6d56e7f6c34bef124374c8f5))
* **internal:** bump rye to 0.44.0 ([#40](https://github.com/Find-AI/find-ai-python/issues/40)) ([ab27996](https://github.com/Find-AI/find-ai-python/commit/ab27996320df9571fbe93108f54eed46cbb83df6))
* **internal:** codegen related update ([d8f0092](https://github.com/Find-AI/find-ai-python/commit/d8f009299bfac2562b14a95263daf0ced6fe3e12))
* **internal:** codegen related update ([#35](https://github.com/Find-AI/find-ai-python/issues/35)) ([5f1f5f3](https://github.com/Find-AI/find-ai-python/commit/5f1f5f3a32c104ae08bffcfde5bd543a4e1678f8))
* **internal:** codegen related update ([#39](https://github.com/Find-AI/find-ai-python/issues/39)) ([8fab104](https://github.com/Find-AI/find-ai-python/commit/8fab1046c0db0b4426a2daaece1b586992b8990f))
* **internal:** exclude mypy from running on tests ([#32](https://github.com/Find-AI/find-ai-python/issues/32)) ([1a805d6](https://github.com/Find-AI/find-ai-python/commit/1a805d682df0a825a2f91c6968b20b5b33b7850a))
* **internal:** expand CI branch coverage ([dbf16dc](https://github.com/Find-AI/find-ai-python/commit/dbf16dc81cce29b630ed18c7cea007f5af7c2e29))
* **internal:** fix compat model_dump method when warnings are passed ([#28](https://github.com/Find-AI/find-ai-python/issues/28)) ([762203b](https://github.com/Find-AI/find-ai-python/commit/762203b6048de50c178f2c3623a6bb6081320f64))
* **internal:** fix list file params ([6ee5b45](https://github.com/Find-AI/find-ai-python/commit/6ee5b457cb32a96ba5e3f8e7f743accd8e0d298c))
* **internal:** import reformatting ([7ed9b68](https://github.com/Find-AI/find-ai-python/commit/7ed9b6812a8d0b94cde0e015455a828301830fea))
* **internal:** minor formatting changes ([25fe185](https://github.com/Find-AI/find-ai-python/commit/25fe185495e80250d999714585aa19b8aad0b4a8))
* **internal:** reduce CI branch coverage ([37e3fd6](https://github.com/Find-AI/find-ai-python/commit/37e3fd6cdd66bf149e90a0c21c8eda8bede292ad))
* **internal:** refactor retries to not use recursion ([410d61c](https://github.com/Find-AI/find-ai-python/commit/410d61c7d62c5325fdcee7f189dd8f16072b7c36))
* **internal:** remove extra empty newlines ([#38](https://github.com/Find-AI/find-ai-python/issues/38)) ([5bee973](https://github.com/Find-AI/find-ai-python/commit/5bee973d3a7b8652298df3097e43df16d9e6b6f3))
* **internal:** remove trailing character ([#45](https://github.com/Find-AI/find-ai-python/issues/45)) ([91f2c95](https://github.com/Find-AI/find-ai-python/commit/91f2c95481fa641f7aef04b90e2b37eb91c912f2))
* **internal:** remove unused http client options forwarding ([#36](https://github.com/Find-AI/find-ai-python/issues/36)) ([c123f30](https://github.com/Find-AI/find-ai-python/commit/c123f300750b010a0b93de2775af65d9ccdb3dbc))
* **internal:** slight transform perf improvement ([#46](https://github.com/Find-AI/find-ai-python/issues/46)) ([122427e](https://github.com/Find-AI/find-ai-python/commit/122427e7e4da17b68364dea3898f95dd532b6be9))
* **internal:** update models test ([1ffac85](https://github.com/Find-AI/find-ai-python/commit/1ffac850048bf119291945b54433af25f1a212f3))
* **internal:** update pyright settings ([adb2e58](https://github.com/Find-AI/find-ai-python/commit/adb2e585ce7edeb87c6d0a29693195b99244dff6))
* rebuild project due to codegen change ([#25](https://github.com/Find-AI/find-ai-python/issues/25)) ([4b86eae](https://github.com/Find-AI/find-ai-python/commit/4b86eaedbd6df8fbb7e94f34e2d1a9b945d3530f))
* rebuild project due to codegen change ([#26](https://github.com/Find-AI/find-ai-python/issues/26)) ([7ec6fa4](https://github.com/Find-AI/find-ai-python/commit/7ec6fa4a8efdb19233d684ea84a4682c0b1da503))
* rebuild project due to codegen change ([#27](https://github.com/Find-AI/find-ai-python/issues/27)) ([9592b91](https://github.com/Find-AI/find-ai-python/commit/9592b916168b1a4b38c2df33a3122a9c712b3b75))
* remove now unused `cached-property` dep ([#31](https://github.com/Find-AI/find-ai-python/issues/31)) ([b4a624b](https://github.com/Find-AI/find-ai-python/commit/b4a624bcd94809dbf465134ca12ccea4e7b8b3dc))


### Documentation

* add info log level to readme ([#29](https://github.com/Find-AI/find-ai-python/issues/29)) ([2adc14e](https://github.com/Find-AI/find-ai-python/commit/2adc14ebdcd2fad48ac2b824dc27175d0871690e))

## 1.2.0 (2024-10-08)

Full Changelog: [v1.0.0...v1.2.0](https://github.com/Find-AI/find-ai-python/compare/v1.0.0...v1.2.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#16](https://github.com/Find-AI/find-ai-python/issues/16)) ([2c12534](https://github.com/Find-AI/find-ai-python/commit/2c12534ff3c1c76caf1ea0a627a76b335c23b5e3))


### Chores

* **internal:** add support for parsing bool response content ([#18](https://github.com/Find-AI/find-ai-python/issues/18)) ([9660e93](https://github.com/Find-AI/find-ai-python/commit/9660e9335272283ad44db1838bdfc0a3afb45815))

## 1.0.0 (2024-10-03)

Full Changelog: [v0.1.0-alpha.1...v1.0.0](https://github.com/Find-AI/find-ai-python/compare/v0.1.0-alpha.1...v1.0.0)

### Features

* **api:** manual updates updated ([#9](https://github.com/Find-AI/find-ai-python/issues/9)) ([b0aca07](https://github.com/Find-AI/find-ai-python/commit/b0aca073da989b196bbf1a3e64b0d47d094b6b3b))
* **api:** OpenAPI spec update via Stainless API ([#11](https://github.com/Find-AI/find-ai-python/issues/11)) ([5d384f6](https://github.com/Find-AI/find-ai-python/commit/5d384f6305f7865191592ee3f337ebfdae8842bd))


### Chores

* **internal:** codegen related update ([#12](https://github.com/Find-AI/find-ai-python/issues/12)) ([1b494da](https://github.com/Find-AI/find-ai-python/commit/1b494da80f2e1344120fbef42dc3792c0833265d))
* **internal:** codegen related update ([#13](https://github.com/Find-AI/find-ai-python/issues/13)) ([7e7831e](https://github.com/Find-AI/find-ai-python/commit/7e7831e72783e50ec538bbd13a80be31f7188df4))

## 0.1.0-alpha.1 (2024-09-25)

Full Changelog: [v0.0.1-alpha.1...v0.1.0-alpha.1](https://github.com/Find-AI/find-ai-python/compare/v0.0.1-alpha.1...v0.1.0-alpha.1)

### Features

* **api:** manual updates ([#5](https://github.com/Find-AI/find-ai-python/issues/5)) ([d46ce50](https://github.com/Find-AI/find-ai-python/commit/d46ce5025103249636ae9a789b67b1c5fc0c717e))
* **api:** OpenAPI spec update via Stainless API ([#7](https://github.com/Find-AI/find-ai-python/issues/7)) ([84d6afd](https://github.com/Find-AI/find-ai-python/commit/84d6afd94a7940075210f03767de0e76caaee225))

## 0.0.1-alpha.1 (2024-09-24)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/Find-AI/find-ai-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* go live ([#1](https://github.com/Find-AI/find-ai-python/issues/1)) ([222eb9c](https://github.com/Find-AI/find-ai-python/commit/222eb9cb10ce5f49a1f03b9e6e6e629bf3baadab))
* update SDK settings ([#3](https://github.com/Find-AI/find-ai-python/issues/3)) ([e58ae3f](https://github.com/Find-AI/find-ai-python/commit/e58ae3f46bac80cc33050298250f66f7d8e8ee2c))
