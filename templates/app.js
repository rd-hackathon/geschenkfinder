// Imports
const express = require('express')
const expressLayouts = require('express-ejs-layouts')

const app = express()
const port = 8082

// Static Files
app.use(express.static('public'))
//app.use('/css', express.static(__dirname + 'public/css'))

// Set Templating Engine
app.use(expressLayouts)
app.set('layout', './layouts/layout')
app.set('view engine', 'ejs')

// Routes
app.get('', (req, res) => {
    res.render('index', { title: 'Geschenke Finder'})
})

app.get('/upload', (req, res) => {
    res.render('upload', { title: 'Upload Data'})
})

app.get('/swipe', (req, res) => {
    res.render('swipe', { title: 'Swipe Geschenk'})
})

app.get('/results', (req, res) => {
    res.render('results', { title: 'Resultate'})
})

app.get('/credits', (req, res) => {
    res.render('credits', { title: 'Credits'})
})

// Listen on Port 5000
app.listen(port, () => console.info(`App listening on port ${port}`))