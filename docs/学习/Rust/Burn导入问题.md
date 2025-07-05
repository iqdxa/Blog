# Burn导入问题
- 日期：2025年7月1日

### 发生时机
在cargo.toml文件中添加依赖：
```toml
burn = { version = "0.17.1", features = ["wgpu"] }
spider = "2.37.126"
```
### 报错
出现报错：
```
error: failed to select a version for `libsqlite3-sys`.
    ... required by package `sqlx-sqlite v0.8.0`
    ... which satisfies dependency `sqlx-sqlite = "=0.8.0"` of package `sqlx v0.8.0`
    ... which satisfies dependency `sqlx = "^0.8"` of package `spider v2.37.126`
    ... which satisfies dependency `spider = "^2.37.126"` of package `rust_test v0.1.0 (C:\Users\TFC\Documents\MyProjects\rust_test)`
versions that meet the requirements `^0.28.0` are: 0.28.0

package `libsqlite3-sys` links to the native library `sqlite3`, but it conflicts with a previous package which links to `sqlite3` as well:
package `libsqlite3-sys v0.32.0`
    ... which satisfies dependency `libsqlite3-sys = "^0.32.0"` of package `rusqlite v0.34.0`
    ... which satisfies dependency `rusqlite = "^0.34.0"` of package `burn-dataset v0.17.1`
    ... which satisfies dependency `burn-dataset = "^0.17.1"` of package `burn-core v0.17.1`
    ... which satisfies dependency `burn-core = "^0.17.1"` of package `burn v0.17.1`
    ... which satisfies dependency `burn = "^0.17.1"` of package `rust_test v0.1.0 (C:\Users\TFC\Documents\MyProjects\rust_test)`
Only one package in the dependency graph may specify the same links value. This helps ensure that only one copy of a native library is linked in the final binary. Try to adjust your dependencies so that only one package uses the `links = "sqlite3"` value. For more information, see https://doc.rust-lang.org/cargo/reference/resolver.html#links.

failed to select a version for `libsqlite3-sys` which could resolve this conflict

```
### 分析
冲突发生在`libsqlite3-sys v0.32.0`这个包。
### 解决
不要同时使用这两个依赖。

在2025年7月1日两个包均使用最新版本，会发生依赖冲突，不知道以后这两个包升级了会不会就不会冲突了。