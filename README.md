This is the repository for the digital preservation webpage and blog.

---

To preview locally. run `hugo server -D` (builds posts and drafts)

See samplepost.md for all available markdown syntax and explanations for frontmatter.

See https://gohugo.io/content-management/organization/

Add new blog posts under content/blog directory. Organize as page bundles if using assets.

```
Content
└── blog
    ├── Post1            <-- Page bundle for post 1
    │   ├── index.md     <------ post in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── Post2            <-- Page bundle for post 2
    │   └── index.md     <------ post in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── posttitle.md     <-- post 3 in markdown (w/ no assets) straight under blog directory
    └── _index.md        <-- index/layout definitions for blog overview page (do not edit)
```

Add new documents under content/documents, similarly to blog posts. These posts only show under the documents-tab.

```
Content
├── documents
    ├── Post1            <-- Page bundle for post 1
    │   ├── index.md     <------ document 1 in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── Document2.md     <-- document 2 in markdown (w/ no assets) straight under blog directory
    └── _index.md        <-- index/layout definitions document overview page (do not edit)
```

