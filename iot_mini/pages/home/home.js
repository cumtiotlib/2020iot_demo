// pages/home/home.js
Page({
    data: {
        id: 'iot',
        ori_img: '',
    },
    onLoad: function (options) {

    },
    upload: function () {
        var that = this
        wx.chooseImage({
            count: 1,
            success: function (res) {
                console.log(res)
                that.setData({
                    ori_img: res.tempFilePaths[0]
                })
                wx.uploadFile({
                    filePath: res.tempFilePaths[0],
                    name: 'images',
                    url: 'http://127.0.0.1:5000/upload',
                    success: function (res) {
                        // console.log(res)
                        console.log(JSON.parse(res.data))
                        that.setData({
                            filename: JSON.parse(res.data).filename
                        })
                    }
                })
            }
        })
    },
    predict: function () {
        var that = this
        wx.request({
            url: 'http://127.0.0.1:5000/predict',
            method: 'post',
            data: {
                filename: that.data.filename
            },
            success: function (res) {
                console.log(res)
                var pre_img = 'http://127.0.0.1:5000/imgs/'
                that.setData({
                    pre_img: pre_img + res.data.filename
                })
            }
        })
    }
})