/* Norantz site script. Version 0.1, 18 November 2026. Zero draft.
   Every page works without it; it only adds the report filters and stops
   the placeholder forms from sending anything. */
(function () {
  // Reports: filter the list by the data attributes on each row.
  var form = document.getElementById('report-filters');
  var list = document.getElementById('report-list');
  if (form && list) {
    var rows = Array.prototype.slice.call(list.querySelectorAll('.nz-rrow'));
    var count = document.getElementById('filter-count');
    var apply = function () {
      var want = {};
      form.querySelectorAll('select[data-filter]').forEach(function (s) { if (s.value) want[s.dataset.filter] = s.value; });
      var shown = 0;
      rows.forEach(function (r) {
        var ok = Object.keys(want).every(function (k) { return r.dataset[k] === want[k]; });
        r.hidden = !ok;
        if (ok) shown++;
      });
      if (count) count.textContent = 'Showing ' + shown + ' of ' + rows.length + ' reports';
    };
    form.addEventListener('change', apply);
    form.addEventListener('reset', function () { setTimeout(apply, 0); });
    // A country link such as ?country=indonesia preselects the filter.
    var q = new URLSearchParams(location.search);
    form.querySelectorAll('select[data-filter]').forEach(function (s) {
      var v = q.get(s.dataset.filter);
      if (v) s.value = v;
    });
    apply();
  }

  // Placeholder forms: nothing is sent in the zero draft.
  document.querySelectorAll('form[data-placeholder]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = f.querySelector('.nz-form-msg');
      if (msg) { msg.hidden = false; msg.focus(); }
    });
  });
})();
