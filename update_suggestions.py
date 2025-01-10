def update_suggestions(self, event=None):
    prefix = self.input_field.get()
    suggestions = self.trie.starts_with(prefix)
    self.suggestions_listbox.delete(0, tk.END)  # Clear previous suggestions
    if suggestions:
        for word in suggestions:
                self.suggestions_listbox.insert(tk.END, word)
    else:
        self.suggestions_listbox.insert(tk.END, "No suggestions found")